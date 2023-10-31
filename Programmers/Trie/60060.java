import java.util.*;

class Solution {

    static class Trie {
        Node root = new Node();

        void insert(String word) {
            Node node = this.root;

            for (int i = 0; i < word.length(); i++) {
                if (!node.child.containsKey(word.charAt(i))) {
                    node.child.put(word.charAt(i), new Node());
                }
                Node nxt = node.child.get(word.charAt(i));
                nxt.checkCnt++;
                node.child.put(word.charAt(i), nxt);
                node = nxt;
            }
        }

        int search(String word) {
            Node cur = this.root;
            int pre_v = 0;
            for (int i = 0; i < word.length(); i++) {
                char s = word.charAt(i);
                if (s == '?') return pre_v;
                if (!cur.child.containsKey(s)) return 0;
                pre_v = cur.child.get(s).checkCnt;
                cur = cur.child.get(s);
            }
            return pre_v;
        }
    }

    static class Node {
        HashMap<Character, Node> child = new HashMap<>();
        int checkCnt = 0;
    }
    public int[] solution(String[] words, String[] queries) {
        int[] answer = new int[queries.length];
        HashMap<Integer, Trie> prefix_dict = new HashMap<>();
        HashMap<Integer, Trie> suffix_dict = new HashMap<>();
        HashMap<Integer, Integer> len_dict = new HashMap<>();

        for (String word : words) {
            Trie preTrie = prefix_dict.get(word.length());
            if (preTrie == null) preTrie = new Trie();
            preTrie.insert(word);
            prefix_dict.put(word.length(), preTrie);

            Trie sufTrie = suffix_dict.get(word.length());
            if (sufTrie == null) sufTrie = new Trie();
            sufTrie.insert(new StringBuffer(word).reverse().toString());
            suffix_dict.put(word.length(), sufTrie);

            Integer cnt = len_dict.get(word.length());
            if (cnt == null) cnt = 0;
            len_dict.put(word.length(), cnt + 1);
        }

        for (int i = 0; i < queries.length; i++) {
            String q = queries[i];
            if (q.charAt(0) == '?' && q.charAt(q.length() - 1) == '?') {
                answer[i] = len_dict.get(q.length()) == null ? 0 : len_dict.get(q.length());
            } else if (q.charAt(q.length() - 1) == '?') {
                Trie preTrie = prefix_dict.get(q.length());
                if (preTrie == null){
                    answer[i] = 0;
                    continue;
                }
                answer[i] = preTrie.search(q);
            } else if (q.charAt(0) == '?') {
                Trie sufTrie = suffix_dict.get(q.length());
                if (sufTrie == null) {
                    answer[i] = 0;
                    continue;
                }
                answer[i] = sufTrie.search(new StringBuffer(q).reverse().toString());
            }
        }

        return answer;
    }
}

// Trie를 구현하되 각 문자마다 접근한 횟수를 업데이트 시켜준다.
// queries에서 각 문자열을 읽다가 물음표를 만나면 바로 이전 문자의 접근 개수를 리턴해 준다.