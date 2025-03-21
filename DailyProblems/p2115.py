# Problem link : https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/?envType=daily-question&envId=2025-03-21

'''
Problem description:
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.
'''
from typing import List
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Graph based solution
        g = {}
        supplies = set(supplies)
        for ind, recipe in enumerate(recipes):
            # Creating an adjacency list representation of the graph
            g[recipe] = ingredients[ind]
        def dfs(r, visited = None):
            if visited is None:
                visited = set()
            if r not in g:
                if r in supplies:
                    return True
                else:
                    return False
            if r in visited:
                return False
            if r in buildable:
                return True
            if r in not_buildable:
                return False
            visited.add(r)
            for n in g[r]:
                if not dfs(n, visited):
                    return False
            visited.remove(r)
            return True
        buildable = set()
        not_buildable = set()
        for r in g.keys():
            if dfs(r):
                buildable.add(r)
            else:
                not_buildable.add(r)
        return list(buildable)


'''
Algorithm explained:
1. Construct a graph (adjacency list) where recipes are keys and values are the ingredients.
2. To check if a recipe is buildable, we give it to a dfs function along with an empty visited set
3. for every node whose neighbours are explored, it adds to the visited and once all the neighbours are explored, then we remove it from visited
4. Here is a simple explanation of why we need to remove the node from visited after exploration
5. consider A depends on B and C. B depends on D and C depends on D. If D is in supplies, then A should be buildable. if we don't remove the node B and D after exploration, then when it encounters C and it's child D, it thinks that there is a cycle even though in reality there is no cycle, so we need to remove the node after exploration.
6. After all the children nodes are buildable, we can exit out with success, if not return Failure.
'''
