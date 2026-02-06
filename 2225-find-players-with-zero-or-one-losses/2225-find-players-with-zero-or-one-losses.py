# Technique used: Hash Map or Frequency Counting
# Time complexity: O(NlogN)
# Space complexity: O(N)

from collections import defaultdict

class Solution(object):
    def findWinners(self, matches):
        loss_count = defaultdict(int)
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loss_count[loser] += 1

        zero_losses = []
        one_loss = []

        for player in players:
            if loss_count[player] == 0:
                zero_losses.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)

        zero_losses.sort()
        one_loss.sort()

        return [zero_losses, one_loss]
