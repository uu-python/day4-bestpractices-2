from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

ranksum = comm.reduce(rank, op=MPI.SUM, root=0)

print("This is rank %d" %rank)
if rank == 0:
    print("Rank %d reports that the sum of ranks is: %d" %(rank,ranksum))
