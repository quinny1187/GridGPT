# GridGPT
Grid GPT is a class you can use in your ChatGPT vision api projects that will allow your ChatGPT with vision to finally give you accurate you coordinates when you ask it to locate specific objects.  This will enable things like allowing ChatGPT vision to accurately control your mouse through the gui and click on things.  There is some extra work to be do to add the translation layer from grid cell to actual button click but that is pretty easy to solve.

#Example 1: Small Image 50 pixel cell size - ask for a single grid
![image](https://github.com/quinny1187/GridGPT/assets/108108975/1421460f-6ae7-4f3a-a44f-d4bee5b1b2dc)

#Example 2: Large 4k Image 100 pixel cell size - ask for group of cell grids
![image](https://github.com/quinny1187/GridGPT/assets/108108975/8b7dcd07-3b52-4b43-9d91-d2d7d2d1bc05)

#How it works
During runtime it takes your image and uses Pillow to
1. Lay down cells of transparent white background. You modify the intensity of this in the code.
2. Draw the grids according to cell size. They should cover the entire picture even if the cell size doesnt divide by your image size correctly.
3. Add in a transparent text identifier so ChatGPT can tell the grids apart.
4. Take the output file and send it to ChatGPT Vision along with the prompt.txt I included(it require two modifications).
5. After some fine tuning of the parameters ChatGPT will be able to tell you exactly what grid cells to click on for the object you are looking for.
