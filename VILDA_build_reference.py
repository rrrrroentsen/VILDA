import os
import subprocess
import argparse

def run_command(command):
    """Run a shell command and print it."""
    print(f"Running command: {command}")
    subprocess.run(command, shell=True, check=True)

def build_star_reference(reference_dir, genome_fa, genome_gtf, threads):
    """Build STAR reference for Homo sapiens genome."""
    os.makedirs(os.path.join(reference_dir, 'GRCh38'), exist_ok=True)
    command = (
        f"STAR --runMode genomeGenerate --runThreadN {threads} "
        f"--genomeDir {os.path.join(reference_dir, 'GRCh38')} "
        f"--genomeFastaFiles {genome_fa} "
        f"--sjdbGTFfile {genome_gtf}"
    )
    run_command(command)
    print("STAR reference for Homo sapiens genome has been built.")

def build_minimap2_index(reference_dir, viral_fa):
    """Build Minimap2 index for VILDA."""
    command = (
        f"minimap2 -d {os.path.join(reference_dir, 'VILDA.mmi')} "
        f"{viral_fa}"
    )
    run_command(command)
    print("Minimap2 index for VILDA has been built. You can start using VILDA now.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build STAR reference and Minimap2 index.")
    parser.add_argument("--reference_dir", required=True, help="Directory to save reference files.")
    parser.add_argument("--genome_fa", required=True, help="Path to Homo sapiens genome FASTA file.")
    parser.add_argument("--genome_gtf", required=True, help="Path to Homo sapiens genome GTF file.")
    parser.add_argument("--viral_fa", required=True, help="Path to viral genome FASTA file.")
    parser.add_argument("--threads", type=int, default=32, help="Number of threads to use for building the reference.")
    
    args = parser.parse_args()
    build_star_reference(args.reference_dir, args.genome_fa, args.genome_gtf, args.threads)
    build_minimap2_index(args.reference_dir, args.viral_fa)
