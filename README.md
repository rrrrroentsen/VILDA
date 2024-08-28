## VILDA

VILDA (Viral RNA Detection and Analysis) is a tool designed for detecting and analyzing viral transcripts in bulkRNA-Seq data.

## Installation

1. **Download Reference Files**:

   Since the reference files are too large to be stored on GitHub, they are hosted on Google Drive. You can download them using the following links:

   - [Homo_sapiens.GRCh38.fa], [Homo_sapiens.GRCh38.111.gtf], [VILDA.fasta], [VILDA.gtf], [VILDA.mmi]
   - https://drive.google.com/drive/folders/1Y4ApWSGvvb6EhItm7unzqUMjBACWk0Lb
 
2. **Unpack Reference Files**:

   After downloading, move all the files to a directory where you plan to store the references, e.g., `/path/to/reference_dir`.

## Usage

### Step 1: Build Reference

Use the following command to build the STAR reference and Minimap2 index:

python VILDA_build_reference.py --reference_dir /path/to/reference_dir \
                                --genome_fa /path/to/Homo_sapiens.GRCh38.fa \
                                --genome_gtf /path/to/Homo_sapiens.GRCh38.111.gtf \
                                --viral_fa /path/to/VILDA.fasta \
                                --threads 56

### Step 2: Detect Viral Transcripts

Once the references are built, you can detect viral transcripts using the following command:

python VILDA_detect_viral_transcripts.py --reference_dir /path/to/reference_dir \
                                         --sample_name SAMPLE_NAME \
                                         --fastq /path/to/fastq1 /path/to/fastq2 \
                                         --output_dir /path/to/output_dir \
                                         --threads 56

## Author Information

VILDA is developed by Xiaosheng Liu (ORCID 0000-0003-4282-5740)

## Additional Notes
For more detailed instructions and examples, please refer to the package documentation.
If you encounter any issues or have suggestions for improvement, please open an issue on GitHub.
This package is provided as-is under the MIT License.
