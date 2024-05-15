/*
/   Project Euler #18 Maximum path sum I
/
/   Find the maximum total from top to bottom of the triangle.
/
*/

import java.io.*;


public class Euler_18
{

    private static String pathBuilder(String triFile)
    {
        String curDir = System.getProperty("user.dir");
        String basePath = "/";
        String[] pathComponents = curDir.split("/");

        for (int i = 1; i < pathComponents.length - 1; i++)
            basePath += pathComponents[i] + "/";

        return basePath + triFile;
    }


    public static void main(String[] args)
    {
        long start = System.nanoTime();
        int maxPath = 0;
        int triFileSize;

        String triFileName = "~/Project-Euler/euler_txt/triangle1.txt";
        String  triFilePath = pathBuilder(triFileName);

        int col;
        int row = 0;
        int[][] pyramid = new int[15][15];

        try {

            FileReader triFileReader = new FileReader(triFilePath);
            BufferedReader triFileBuffer = new BufferedReader(triFileReader);

            String triLine;
            String[] triLineBuffer;
            int[] pyramidRow;

            while ((triLine = triFileBuffer.readLine()) != null) {

                triLineBuffer = triLine.split(" ");
                col = 0;
                pyramidRow = new int[triLineBuffer.length];

                for (int i = 0; i < triLineBuffer.length; i++) {
                    if (!triLineBuffer[i].equals(""))
                        pyramidRow[col++] = Integer.parseInt(triLineBuffer[i]);
                }

                pyramid[row++] = pyramidRow;
            }
        }

        catch (FileNotFoundException err) {
            System.out.printf("Error opening %s: %s\n", triFilePath, err);
        }

        catch (IOException err) {
            System.out.printf("Error reading %s: %s\n", triFilePath, err);
        }

        int pyramidHeight = row;

        row = col = 0;

        maxPath += pyramid[row][col];

        int colL, colR;

        while (row < pyramidHeight - 2) {

            colL = pyramid[row + 2][col] > pyramid[row + 2][col + 1] ?
                   pyramid[row + 2][col] : pyramid[row + 2][col + 1];

            colR = pyramid[row + 2][col + 1] > pyramid[row + 2][col + 2] ?
                   pyramid[row + 2][col + 1] : pyramid[row + 2][col + 2];

            if ((pyramid[row + 1][col + 1] + colR) >
                (pyramid[row + 1][col] + colL)) {
                maxPath += pyramid[row + 1][col + 1];
                col++;
            } else {
                maxPath += pyramid[row + 1][col];
            }

            row++;
        }

        if (pyramid[row + 1][col] > pyramid[row + 1][col + 1])
            maxPath += pyramid[row + 1][col];
        else
            maxPath += pyramid[row + 1][col + 1];

        long stop = System.nanoTime();
        System.out.println("Answer: " + maxPath);
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }
}
