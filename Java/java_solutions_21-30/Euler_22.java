/*
/   Project Euler problem #22 Name scores
/
/   What is the total of all the name scores in the file?
/
*/

import java.io.*;


public class Euler_22
{

    public static String pathBuilder(String fname)
    {
        String cwd = System.getProperty("user.dir");
        String[] pathComponents = cwd.split("/");
        String path = "";

        for (int i = 1; i < pathComponents.length - 1; i++)
            path += "/" + pathComponents[i];
        
        return path + "/" + fname;
    }

    public static String[] nameSorter(String names[])
    {
        for (int i = 0; i < names.length; i++) {
            String cur = names[i];
            int j = i - 1;
            while (j >= 0 && cur.compareTo(names[j]) < 0) {
                names[j + 1] = names[j];
                j--;
            }

            names[j + 1] = cur;
        }

        return names;
    }

    public static void main(String[] args)
    {
        long nameScores = 0;

        String fname = "euler_txt/names1.txt";
        String path = pathBuilder(fname);
        String fileData = "";

        try {
            FileReader fReader = new FileReader(path);
            BufferedReader fHandle = new BufferedReader(fReader);

            int fileChar;

            while ((fileChar = fHandle.read()) != -1)
                fileData += (char) fileChar;
        } 
        
        catch (FileNotFoundException err) {
            System.out.printf("Error opening %s: %s\n", path, err);
        }

        catch (IOException err) {
            System.out.printf("Error reading %s: %s\n", path, err);
        }

        String[] fileNames = fileData.split(",");
        for (int i = 0; i < fileNames.length; i++) { 
            fileNames[i] = fileNames[i].replace("\"", ""); 
        }

        fileNames = nameSorter(fileNames);
        for (int i = 0; i < fileNames.length; i++) {
            long nameScore = 0;
            for (int j = 0; j < fileNames[i].length(); j++)
                nameScore += ((int) fileNames[i].charAt(j) - 64);
            nameScore *= (i + 1);
            nameScores += nameScore;
        }

        System.out.println("Answer: " + nameScores);
    }
}
