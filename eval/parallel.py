import multiprocessing as mp


def run_many(fn, jobs, processes=2):
    """fn(*job) for every job, one fresh process per job; returns results in order."""
    ctx = mp.get_context("spawn")
    with ctx.Pool(processes=processes, maxtasksperchild=1) as pool:
        return pool.starmap(fn, jobs, chunksize=1)
