import java.io.*;
import java.util.*;

public class anon2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[][] points = new int[N][2];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            points[i][0] = Integer.parseInt(st.nextToken());
            points[i][1] = Integer.parseInt(st.nextToken());
        }

        ArrayList<dist> dist = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                dist temp = new dist(i, j, dist(points[i][0], points[i][1], points[j][0], points[j][1]));
                dist.add(temp);
            }
        }
        dist.sort(Comparator.comparingLong(a -> a.dist));
        boolean good = false;
        long min = dist.get(0).dist;
        loop:
        for (int i = 0; i < N; i++) {
            if (dist.get(i).dist != min) {
                break;
            }
            for (int j = i + 1; j < N; j++) {
                if (dist.get(j).dist != min) {
                    break;
                }
                if (dist.get(j).a != dist.get(i).a && dist.get(j).a != dist.get(i).b && dist.get(j).b != dist.get(i).a && dist.get(j).b != dist.get(i).b) {
                    good = true;
                    break loop;
                }
            }
        }
        if (good) {
            pw.println(1);
        } else {
            HashSet<Integer> temp = new HashSet<>();
            for (int i = 0; i < N; i++) {
                if (dist.get(i).dist != min) {
                    break;
                }

                temp.add(dist.get(i).a);
                temp.add(dist.get(i).b);
            }
            ArrayList<Integer> all = new ArrayList<>(temp);
            Collections.sort(all);
            double max = 0;
            int maxNum = 0;
            for (Integer cur : all) {
                for (dist d : dist) {
                    if (d.a != cur && d.b != cur) {
                        if (d.dist > max) {
                            max = d.dist;
                            maxNum = cur;
                        }
                        break;
                    }
                }
            }
            pw.println(maxNum + 1);
        }

        pw.close();
    }

    private static long dist(long ax, long ay, long bx, long by) {
        return (ax - bx) * (ax - bx) + (ay - by) * (ay - by);
    }

    private static class dist {
        int a, b;
        long dist;

        private dist(int a, int b, long dist) {
            this.a = a;
            this.b = b;
            this.dist = dist;
        }
    }
}