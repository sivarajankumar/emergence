## Overview ##

Currently in the design and initial development phase, Emergence is a biological sequence annotation and analysis system designed to provide analysis, curation and data visualization all within the same package.  It has a strong focus on integration of existing tools and frameworks over reinventing the wheel.

Emergence is written using Python3 and the Django web framework on the server-side, with a UI implemented using AngularJS, HTML5, and CSS3.  Its development has been guided by the needs of active projects in eukaryotic annotation, RNA-Seq, SNP analysis and metagenomics.

## First release targets ##

Progress will be continually committed here, and the next release target coinciding with its second presentation at Genome Informatics 2013 in late October.  The target features for the next release include:

  * Formalized tool dependency system with input/output type classifications
  * Local command execution and monitoring
  * Distributed command processing via Grid Engine
  * Galaxy API integration layer
  * Ergatis API integration layer
  * Initial tool/pipeline support for:
    * Prokaryotic gene finders: Prodigal and Glimmer
    * Eukaryotic gene finders: Augustus and Genemark-ES
    * Digital read normalization (khmer analysis)
    * RNA-seq assembly: Trinity
    * SNP analysis pipeline (via Galaxy)
    * Prokaryotic structural and functional pipeline (via Ergatis)
    * Eukaryotic protein functional pipeline (via Ergatis)
    * Result visualization with JBrowse

## Try out the current code ##

Although there isn't a packaged release yet, you can run through an example pipeline with the development version now.  See the [GettingStarted](GettingStarted.md) guide.