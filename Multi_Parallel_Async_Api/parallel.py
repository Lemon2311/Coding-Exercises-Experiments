import os 
import multiprocessing

num_threads = multiprocessing.cpu_count()
os.system(f"hypercorn main:app --bind 0.0.0.0:420 --workers {num_threads}")
