/*
/   Project Euler problem #25 1000-digit Fibonacci number
/
/   What is the index of the first term in the Fibonacci sequence to contain
/   1000 digits?
/
*/

import java.math.BigInteger;
import java.util.Iterator;


public class Euler_25<T> implements Iterable<T>
{
    public Iterator iterator() 
    { return new fibonacciGen(); }

    private class fibonacciGen implements Iterator<T>
    {
        private BigInteger current;
        private BigInteger previous;
        private int fibonacciLimit;

        private fibonacciGen()
        {
            current = new BigInteger("1");
            previous = new BigInteger("1");

            fibonacciLimit = 1000;
        }

        public T next()
        {
            if (!hasNext())
                throw new java.util.NoSuchElementException();

            BigInteger tmp = previous;
            previous = current;
            current = current.add(tmp);

            return (T) current;
        }                        

        public boolean hasNext()
        { return current.toString().length() < fibonacciLimit; }

        public void remove()
        { throw new UnsupportedOperationException(); }
    }

    public static void main(String[] args)
    {
        int idxFibonacci = 0;

        Euler_25<BigInteger> euler = new Euler_25<BigInteger>();
        Iterator fibonacciIter = euler.iterator();

        for (idxFibonacci = 1; fibonacciIter.hasNext(); 
             fibonacciIter.next(), idxFibonacci++);

        System.out.println("Answer: " + ++idxFibonacci);
    }
}
