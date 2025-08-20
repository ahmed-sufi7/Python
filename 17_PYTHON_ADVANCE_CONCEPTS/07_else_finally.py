try:
   a = 34/0
except Exception as e:
   print(e)

else:
   print("No errors occurred.")


finally:
   print("Execution completed.")