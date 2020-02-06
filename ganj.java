import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.*;

public class Main {
    private static long[][] vals;
    private static int[][] group;

    private static boolean bekr(int i, int j) {
        return vals[i][j] != 0 && group[i][j] == -1;
    }

    public static void main(String[] args) throws FileNotFoundException {
//        InputStream input = new FileInputStream("/Users/mehdi/Desktop/untitled/1.in");
//        Scanner scanner = new Scanner(input);
        Scanner scanner = new Scanner(System.in);
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        vals = new long[n][m];
        group = new int[n][m];
        int g_sec = 0;
        Map<Integer, Long> islands = new HashMap<>();
        islands.put(-1, 0L);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                vals[i][j] = scanner.nextLong();
                group[i][j] = -1;
            }
        Stack<int[]> pending = new Stack<>();
        for (int k = 0; k < n; k++)
            for (int l = 0; l < m; l++)
                if (bekr(k, l)) {
                    pending.push(new int[]{k, l, g_sec});
                    long c = 0;
                    while (pending.size() > 0) {
                        int[] params = pending.pop();
                        int i = params[0], j = params[1], g = params[2];
                        if (bekr(i, j)) {
                            group[i][j] = g;
                            c = Math.addExact(c, vals[i][j]);
                            for (int[] dir : dirs) {
                                int ni = i + dir[0], nj = j + dir[1];
                                if ((ni >= 0 && ni < n) && (nj >= 0 && nj < m))
                                    if (bekr(ni, nj))
                                        pending.push(new int[]{ni, nj, g});
                            }
                        }
                    }
                    islands.put(g_sec++, c);
                }
        System.out.println();
        System.out.println(Collections.max(islands.values()));
    }
}