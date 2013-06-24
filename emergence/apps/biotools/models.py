from django.db import models

"""
This module is used to describe bioinformatics tools, their formats, and interdependencies.
"""

class Filetype( models.Model ):
    """
    Base class for the different bioinformatics file types, such as GFF3, GBK, BAM, etc.

    Attributes:

    - name: This is essentially just a label.
    - format: The main identity of a format (GFF3, BAM, etc.)
    - variant: Should be considered dialects of the primary format (either because there is a
               disagreement on the standard or for the tools which just get it wrong.  If not
               specified) or can describe content-specific versions.  The default value is
               "canonical".
    - spec_url: A URL most accepted as describing the format specification for this file type.
    """
    name      = models.CharField( max_length=100 )
    format    = models.CharField( max_length=100 )
    variant   = models.CharField( max_length=100, default="canonical" )
    spec_url  = models.URLField()


class Tool( models.Model ):
    """
    A 'tool' is an extremely generic term within this framework.  It can represent a single
    executable such as blastn or a more complete analysis pipeline implemented in workflow
    frameworks like Galaxy or Ergatis.  (Of course, this means tools can be made up of other tools.)

    Most simply, a tool should be thought of us a unit of analysis that can require some number
    of inputs and generates at least one output.
    """

    ## Do not include version numbers in the name
    name = models.CharField( max_length=100 )

    ## Pretty open here - could be like '1.12.0' or 'beta5'
    version = models.CharField( max_length=50 )

    ## should be loaded from a discovery/conf file
    exec_path = models.FilePathField( allow_folders=False )

    ## Usually the primary site of the tool by the author
    primary_site = models.CharField( max_length=200 )

    ## Publication (may or may not be peer-reviewed)
    publication = models.CharField( max_length=300 )

    ## note: https://docs.djangoproject.com/en/dev/topics/db/models/#extra-fields-on-many-to-many-relationships
    files = models.ManyToManyField( Filetype, through='ToolFiletype' )


class StandaloneTool( Tool ):
    pass

class ErgatisTool( Tool ):
    pass

class GalaxyTool( Tool ):
    pass



class ToolFiletype( models.Model ):
    """
    Model which links Tools and their associated file types, both input and output.
    """
    tool = models.ForeignKey(Tool)
    filetype = models.ForeignKey(Filetype)
    description = models.CharField( max_length=200 )
    required = models.BooleanField()

    IO_TYPES = (
        ('o', 'Output'),
        ('i', 'Input'),
    )
    io_type = models.CharField( max_length=1, choices=IO_TYPES )



