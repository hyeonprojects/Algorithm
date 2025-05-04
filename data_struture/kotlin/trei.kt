class TrieNode(val char: Char) {
    val children: MutableMap<Char, TrieNode> = mutableMapOf()
    var isEndOfWord: Boolean = false
}

class Trie {
    private val root = TrieNode(' ')

    // 단어 삽입
    fun insert(word: String) {
        var current = root
        for (char in word) {
            current = current.children.getOrPut(char) { TrieNode(char) }
        }
        current.isEndOfWord = true
    }

    // 단어 검색
    fun search(word: String): Boolean {
        var current = root
        for (char in word) {
            val node = current.children[char] ?: return false
            current = node
        }
        return current.isEndOfWord
    }

    // 접두사 검색
    fun startsWith(prefix: String): Boolean {
        var current = root
        for (char in prefix) {
            val node = current.children[char] ?: return false
            current = node
        }
        return true
    }
}