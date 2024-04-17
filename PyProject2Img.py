import os
import sys
if len(sys.argv) !=2 or not os.path.exists(sys.argv[1]):
    print("wrong python project directory!")
else:
    # batch 
    for root,ds,fs in os.walk(sys.argv[1]):
        for f in fs:
            if os.path.splitext(f)[-1] == ".py":
                # get python file url
                py_file_path = os.path.join(root,f)
                os.system("carbon-now {} --save-as {} --save-to {}".format(str(py_file_path),os.path.splitext(f)[0],root))
                os.remove(py_file_path)
