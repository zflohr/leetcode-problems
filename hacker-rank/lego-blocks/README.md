# Lego Blocks

You have an infinite number of 4 types of lego blocks of sizes given as (depth x
height x width):

<pre>
d h w
1 1 1
1 1 2
1 1 3
1 1 4
</pre>

Using these blocks, you want to make a wall of height **n** and width **m**.
Features of the wall are:

- The wall should not have any holes in it.
- The wall you build should be one solid structure, so there should not be a
  straight vertical break across all rows of bricks.
- The bricks must be laid horizontally.

How many ways can the wall be built?

## Example

**n = 2**  
**m = 3**

The height is **2** and the width is **3**. Here are some configurations:

<img src="https://s3.amazonaws.com/hr-assets/0/1526322298-72d127a6f7-bricks.png" alt="example configurations">

These are not all of the valid permutations. There are **9** valid permutations
in all.

## Function Description
Complete the logoBlocks function in the editor below.

legoBlocks has the following parameter(s):
- int n: the height of the wall
- int m: the width of the wall

**Returns**

-int: the number of valid wall formations modulo **(10<sup>9</sup> + 7)**

**Input Format**

The first line contains the number of test cases **t**. Each of the next **t**
lines contains two space-separated integers **n** and **m**.

**Constraints**

**1 <= t <= 100**  
**1 <= n, m <= 1000**

**Sample Input**
<pre>
STDIN   Function
----    --------
4       t = 4
2 2     n = 2, m = 2
3 2     n = 3, m = 2
2 3     n = 2, m = 3
4 4     n = 4, m = 4
</pre>

**Sample Output**
<pre>
3
7
9
3375
</pre>

**Explanation**

For the first case, we can have:

<img src="https://s3.amazonaws.com/hr-assets/0/1526322982-b16b20303f-legosample.png">

**3 mod (10<sup>9</sup> + 7) = 3**

For the second case, each row of the wall can contain either two blocks of width
1, or one block of width 2. However, the wall where all rows contain two blocks
of width 1 is not a solid one as it can be divided vertically. Thus, the number
of ways is **2 x 2 x 2 - 1 = 7** and **7 mod (10<sup>9</sup> + 7) = 7.**

## HackerRank Submission:
See here: https://www.hackerrank.com/challenges/one-week-preparation-kit-lego-blocks/submissions/code/400144737
