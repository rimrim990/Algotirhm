class Solution {
    public long solution(int w, int h) {
        long answer = (long) w * h;

        int divisor = gcd(Math.max(w, h), Math.min(w, h));
        int mw = w / divisor;
        int mh = h / divisor;

        int count = calculate(mw, mh);

        return answer - count * divisor;
    }

    private int calculate(int mw, int mh) {
        int cnt = 0;
        double delta = ((double) mh / mw) * (-1);

        for (int i=0; i<mw; i++) {
            int top = (int) (delta * i + mh) + 1;
            int bottom = (int) (delta * (i+1) + mh) ;

            if (mh - top > 0)
                cnt += mh - top;

            cnt += bottom;
        }
        return mw * mh - cnt;
    }

    private int gcd(int a, int b) {
        while (b > 0) {
            int tmp = b;
            b = a % b;
            a = tmp;
        }

        return a;
    }
}