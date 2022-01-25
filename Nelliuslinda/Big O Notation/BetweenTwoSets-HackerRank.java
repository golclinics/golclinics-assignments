package com.company;

import java.util.Arrays;
import java.util.List;

public class Main {
    //Function to find GCD
    static int findGCD(int n1, int n2) {
        if (n2 == 0) {
            return n1;
        }
        return findGCD(n2, n1 % n2);
    }

    //Function to find LCM
    static int findLCM(int n1, int n2) {
        if (n1 == 0 || n2 == 0)
            return 0;
        else {
            int gcd = findGCD(n1, n2);
            return Math.abs(n1 * n2) / gcd;
        }
    }

    public static int getTotalX(List<Integer> a, List<Integer> b) {
        int result = 0;

        // Call LCM function to get lcm of array a
        int lcm = a.get(0);
        for (Integer integer : a) {
            lcm = findLCM(lcm, integer);
        }

        // Call GCD function to find gcd of array b
        int gcd = b.get(0);
        for (Integer integer : b) {
            gcd = findGCD(gcd, integer);
        }

        // Find common multiple of LCM that can divide GCD
        int cm = 0;
        while (cm <= gcd) {
            cm += lcm;

            if (gcd % cm == 0)
                result++;
        }

        return result;
    }
    public static void main(String[] args) {

        List<Integer>a = Arrays.asList(2,4);
        List<Integer>b = Arrays.asList(16,32,96);

        System.out.println(getTotalX(a,b));
    }
}
