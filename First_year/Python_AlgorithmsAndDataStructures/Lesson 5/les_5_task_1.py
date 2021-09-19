#%%
import timeit

x=2+2
print(timeit.timeit('x=2+2'))
# %%

# python -m timeit -n 100 -s "import sample_timeit"