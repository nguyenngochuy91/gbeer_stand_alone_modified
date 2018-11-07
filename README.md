GBEER_standalone
==========

Overview
--------

GBEER_standalone is a tool to quantify and visualize the evolutionary changes that occur in gene blocks.
GBEER_standalone is designed to be run from the command line, or as part of a web installation, and has tools
and options designed to accomodate these two roles. 

Released under GPL version 3 licence. See http://www.gnu.org/licenses/lgpl.html or
LICENSE for more details.

Requirements
------------
* Python 2.7.6+
* Biopython 1.63+ (python-biopython)
* matplotlib 1.4.3+ (python-matplotlib)
* Levenshtein (python-levenshtein)
* ClustalW (clustalw) - likely replaced with ClustalOmega (clustalo)
* ncbi-tools (ncbi-tools-bin)
* BLAST2 (blast2)
To be tested as requirements
* BLAST+ (ncbi-blast+) - this might not be necessary, i am going to check this dependency explicitly soon
* CD-hit (cd-hit) - not required yet, but will be soon

To install these requirements in a single line, copy the following to a command line window:
```bash
sudo apt-get install python-biopython python-matplotlib python-levenshtein clustalw ncbi-tools-bin blast2 ncbi-blast+ cd-hit muscle
```

Downloading GBEER_standalone
----------------------

GBEER_standalone is stored in a git repository, therefore you should install Git in order
to more easily update this software in the future, and continue folowing this guide.

To install these requirements in a single line, copy the following to a command line window:
```bash
sudo apt-get install git
```

Once this is installed you can download the latest version of the project using the command

```bash
git clone https://github.com/nguyenngochuy91/gbeer_stand_alone_modified.git
```

To update the software package you need to change to the directory that you stored the 
GBEER_standalone application can run the following command.  Git will check for updates
and make any changes needed to keep the software up-to-date.

```bash
git pull
```

 Downloading additional data
----------------------------

With the project we have included a small dataset from proteobacteria. If you are
interested in using a larger dataset, you can run the **download.py** file to download all
the bacteria files that are the latest and the complete ones.You can run the program as following:
```bash
./download.py
```

Additionally it can be downloaded using a browser from the following address.
ftp://ftp.ncbi.nih.gov/genomes/Bacteria/all.gbk.tar.gz - This file is 7.6 GB as of August, 2015



Running GBEER_standalone
-------------------------

The easiest way to run the project is to execute the script named 'gbeer_standalone.py'.  The defaults
that are provided are sufficient to run the project with the data provided.  The results will be placed into a 
directory called './test_run/'

Each accompanying script can be run on its own as well, and each help for each script can be found by
using the -h or --help option.


gbeer_standalone.py -h
usage: gbeer_standalone.py [-h] [-i FILE] [-G DIRECTORY] [-o DIRECTORY]
                           [-f FILE] [-n INT] [-m INT] [-g INT] [-e FLOAT]
                           [-t FILE] [-c] [-q] [-d DIRECTORY]

The purpose of this script is to run the full software suite that we have
developed to study gene blocks using as few inputs as possible. This will
facilitate the ease of use as much as possible.

optional arguments:
  -h, --help            show this help message and exit
  -i FILE, --gene_block_file FILE
                        Input file for the gene block query step of the
                        pipeline.
  -G DIRECTORY, --genbank_directory DIRECTORY
                        Folder containing all genbank files for use by the
                        program.
  -o DIRECTORY, --outfolder DIRECTORY
                        Folder where results will be stored.
  -f FILE, --filter FILE
                        File restrictiong which accession numbers this script
                        will process. If no file is provided, filtering is not
                        performed.
  -n INT, --num_proc INT
                        Number of processors that you want this script to run
                        on. The default is every CPU that the system has.
  -m INT, --min_genes INT
                        Minum number of genes that an gene_block must contain
                        before it can be considered for further analysis. The
                        default is 5 because that is what we are currently
                        using in the study.
  -g INT, --max_gap INT
                        Size in nucleotides of the maximum gap allowed between
                        genes to be considered neighboring. The default is
                        500.
  -e FLOAT, --eval FLOAT
                        eval for the BLAST search.
  -t FILE, --tree FILE  Newick format tree file which will be used to bypass
                        tree creation.
  -c, --clean           Flag to toggle the removal of intermediate files that
                        are unnecessary for analysis, reducing the storage
                        requirements for a run.
  -q, --quiet           Suppresses most program text outputs.
  -d DIRECTORY, --db DIRECTORY
                        Directory where protein BLAST db are stored.
