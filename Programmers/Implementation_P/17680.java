class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        String[] cache = new String[cacheSize];
        if (cacheSize == 0) {
            return cities.length * 5;
        }
        for (String city : cities) {
            city = city.toUpperCase();
            int flag = checkExists(cache, city);
            // cache miss!
            if (flag == -1) {
                // LRU실행
                cache = LRU(cache, cacheSize-1);
                cache[0] = city;
                answer = answer + 5;
                continue;
            }
            // cache hit!
            // 해당 target을 cache 맨앞으로 이동
            cache = LRU(cache, flag);
            answer++;
            cache[0] = city;
        }
        return answer;
    }
    
    public int checkExists(String[] c, String target) {
        for (int i=0; i<c.length; i++) {
            if (c[i] == null) {
                return -1;
            }
            if (c[i].equals(target)) {
                return i;
            }
        }
        return -1;
    }
    
    public String[] LRU(String[] cache, int idx) {
        while (idx != 0) {
            cache[idx] = cache[idx-1];
            idx--;
        }
        return cache;
    }
}

// LRU알고리즘을 이용하는 문제
// LRU의 특징을 알면 그리 어렵지 않은 문제였음