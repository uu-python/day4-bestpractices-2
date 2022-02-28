from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
rank_sums = np.array([rank])
total = np.array([0])

comm.Reduce(rank_sums, total, MPI.SUM, root=0)

if rank == 0:
    print(total)
