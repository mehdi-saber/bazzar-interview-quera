import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(), m = scanner.nextInt();
        long[] s1 = new long[n], s2 = new long[m];
        for (int i = 0; i < n; i++)
            s1[i] = scanner.nextLong();
        for (int i = 0; i < m; i++)
            s2[i] = scanner.nextLong();

        Arrays.sort(s1);
        Arrays.sort(s2);
        List<Long> intersection = new LinkedList<>();
        for (int i = 0, j = 0; i < n && j < m; ) {
            if (s1[i] > s2[j])
                j++;
            else if (s1[i] < s2[j])
                i++;
            else {
                intersection.add(s1[i]);
                i++;
                j++;
            }
        }
        StringBuilder sb = new StringBuilder();
        intersection.forEach(i -> sb.append(i).append(' '));
        System.out.println(intersection.size());
        System.out.println(sb.toString());
    }
}