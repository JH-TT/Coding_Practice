import java.util.*;

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        Arrays.sort(arrayA);
        Arrays.sort(arrayB);
        int minA = arrayA[0];
        int minB = arrayB[0];
        
        List<Integer> dividorA = findDividor(arrayA, minA);
        List<Integer> dividorB = findDividor(arrayB, minB);
        
        int targetA = findNotDividor(arrayA, dividorB);
        int targetB = findNotDividor(arrayB, dividorA);
        
        return Math.max(targetA, targetB);
    }
    
    public List<Integer> findDividor(int[] array, int min) {
        List<Integer> dividor = new ArrayList<>();
        for(int i=2; i<min/2+1; i++) {
            if(!isAllDivide(array, i)){
                continue;
            }
            dividor.add(i);
        }
        if(isAllDivide(array, min)) {
            dividor.add(min);
        }
        return dividor;
    }
    
    public int findNotDividor(int[] array, List<Integer> dividor) {
        Collections.reverse(dividor);
        for(int d : dividor) {
            if(isNotDivide(array, d)) {
                return d;
            }
        }
        return 0;
    }
    
    public boolean isAllDivide(int[] array, int d) {
        for(int a : array) {
            if(a % d != 0) {
                return false;
            }
        }
        return true;
    }
    
    public boolean isNotDivide(int[] target, int d){
        for(int t : target) {
            if(t % d == 0) {
                return false;
            }
        }
        return true;
    }
}

// 파이썬으로만 하니까 숫자 범위가 1억이어도 그냥 n/2정도로 해도 풀린다는게 좋다고 느낌.