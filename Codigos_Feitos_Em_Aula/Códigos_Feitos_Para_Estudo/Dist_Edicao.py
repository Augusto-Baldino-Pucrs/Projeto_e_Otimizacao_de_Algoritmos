def ed(S: str, T:str) -> int:
    memo = {}

    def dp(i:int,j:int) -> int:
        if(i,j) in memo:
            return memo[(i,j)]
        
        #Casos base
        if i ==0:
            return j
        if j == 0:
            return i
        
        if S[i-1] == T[j-1]:
            cost = dp(i-1,j-1)
        else:
            substitute = dp(i-1,j-1)+1
            insert = dp(i,j-1)+1
            delete = dp(i-1,j)+1
            cost = min(substitute,insert,delete)

        memo[(i,j)] = cost
        return cost
    return dp(len(S),len(T))



s1 = "Casablanca"
s2 = "Portentoso"

s3 = "Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to " +"simplify the build processes in the Jakarta Turbine project. There were several" + " projects, each with their own Ant build files, that were all slightly different." +"JARs were checked into CVS. We wanted a standard way to build the projects, a clear "+ "definition of what the project consisted of, an easy way to publish project information" + "and a way to share JARs across several projects. The result is a tool that can now be" + "used for building and managing any Java-based project. We hope that we have created " + "something that will make the day-to-day work of Java developers easier and generally help " + "with the comprehension of any Java-based project."

s4 = "This post is not about deep learning. But it could be might as well. This is the power of " + "kernels. They are universally applicable in any machine learning algorithm. Why you might" + "ask? I am going to try to answer this question in this article." + "Go to the profile of Marin Vlastelica Pogančić" + "Marin Vlastelica Pogančić Jun";


print("Primeiro caso: " + str(ed(s1, s2)))
print("Segundo caso: " + str(ed(s3, s4)))
