class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        # [w, l]
        
        zero_loss = []
        one_loss = []
        
        # look up if current player is in the dict  { player : losses}
        losses = {}
        
        for i in matches:
            player1, player2 = i[0], i[1]
            
            if player1 not in losses:
                losses[player1] = 0
            
            losses[player2] = losses.get(player2, 0) + 1
        
        for p in losses:
            if losses[p] == 0:
                zero_loss.append(p)
            if losses[p] == 1:
                one_loss.append(p)
        zero_loss.sort()
        one_loss.sort()
        
        return [zero_loss, one_loss]
        