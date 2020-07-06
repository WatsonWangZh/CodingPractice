// 请实现一个函数用来匹配包括'.'和'*'的正则表达式。
// 模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
// 在本题中，匹配是指字符串的所有字符匹配整个模式。
// 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。

// 样例
// 输入：
// s="aa"
// p="a*"
// 输出:true


// 递归解法：
// 与一般字符串匹配不同的是，这题多了.和星号两个匹配符；对于.可以匹配任何字符，处理较为简单，但是对于星号处理较为复杂。
// 为了分类更加简洁，我们在比较s[a]与p[b]时，不先去比较这二者是否相等，而是去判断p[b+1]是否为星号，
// 不为星号的话，直接比较s[a]和p[b]，匹配时指针均右移，
// 如果p[b+1]等于星号，那么我们分以下几种情况：
// 1.s[a] != p[b]，意味着如果星号不表示把p[b]出现次数置为0，那么就不匹配，所以此时我们考虑下一种状态match(s,p,a,b+2)。
// 2.s[a] == p[b]，此时就是不确定性有限状态机问题了，我们可以进一步转化为三种状态。
// 第一种：和1一样，即使当前字符匹配，我们还是让它出现的次数为0，说不定p后面的字符还会和s当前字符匹配呢，这种情况我们容易忽略，
// 也就是match(s,p,a,b+2)。
// 第二种：星号使得p[b]出现一次，也就是b直接右移两位进行比较即可。即match(s,p,a+1,b+2)。
// 第三种：星号使得p[b]出现不小于2次，那么可以递归的转化为子问题，b不变，a右移一位。即match(s,p,a+1,b)。
// 如何说上面分类比较难以想到的话，那么这题的边界情况同样需要小心翼翼，稍微出错便不能ac。
// s与p都为空，匹配，但是s为空也可以匹配p不为空，比如p为2星号，星号可以让前面字符出现次数变为0。
// 当然，一旦模式串p为空，而s非空，那么肯定是不匹配的。
// 从下面代码可以看见，边界情况用了两条语句，在b刚刚越界时判断一下a是否也越界了；另外，由于分类时首先考虑的是p[b+1]，
// 所以还需要判断b是否是最后一个字符，如果是，只有在a也到达最后的字符且匹配整体才匹配。

#include<string>
using namespace std;
class Solution {
public:
    bool isMatch(string s, string p) {
        if(!p.size())  return !s.size();
        return match(s,p,0,0);
    }
    bool match(string s,string p,int a,int b){
        if(b == p.size())   return a == s.size();
        if(b + 1 == p.size())   return a + 1 == s.size() && (s[a] == p[b] || p[b] == '.');
        if(p[b+1] != '*'){
            if(s[a] == p[b] || p[b] == '.')    return match(s,p,a+1,b+1);
            return false;
        }
        if(s[a] != p[b] && p[b] != '.')    return match(s,p,a,b+2);
        return match(s,p,a,b+2) || match(s,p,a+1,b+2) || match(s,p,a+1,b);
    }
};
