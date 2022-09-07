from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def main(fnames_consensus, fname_merged_out):


with open(fname_merged_out, 'w') as out_f:
    my_seqs = []
    for fname_consensus in fnames_consensus:
        experiment = fname_consensus.split("/")[-5]
        patient = fname_consensus.split("/")[-4]
        date = fname_consensus.split("/")[-3]

        print('experiment ', experiment)
        print('patient ', patient)
        print('date ', date)

        for record in SeqIO.parse(fname_consensus, 'fasta'):

            new_seq = str(record.seq)
            my_seqs.append(SeqRecord(Seq(new_seq), id = experiment+'-'+patient'-'+date))

    SeqIO.write(my_seqs, out_f, "fasta")


if __name__ == "__main__":
    main(
        snakemake.input.fnames_consensus,
        snakemake.output.fname_merged,
    )
