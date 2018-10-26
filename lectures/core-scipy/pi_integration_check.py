# calculate pi using numerical integration and check result against numpy constant np.pi

print(integrate_to_pi(1.0))

# compare with numpy pi
print(np.pi - integrate_to_pi(1.0))

# can try timing... (uncomment line below)
# %timeit integrate_to_pi(1.0) 
