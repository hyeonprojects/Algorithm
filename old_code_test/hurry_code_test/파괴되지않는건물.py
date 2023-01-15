def solution(board, skill):
    # board 갮수에 맞는 행렬을 생성
    tboard = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    print(tboard)
    # skill에 맞는 지점에 계산합니다. (누적합 관련 있을듯)
    for typ, r1, c1, r2, c2, degree in skill:
        tboard[r1][c1]+=(2*typ-3)*degree
        tboard[r2+1][c2+1]+=(2*typ-3)*degree
        tboard[r2+1][c1]-=(2*typ-3)*degree
        tboard[r1][c2+1]-=(2*typ-3)*degree
    print(tboard)
    for i in range(1, len(tboard[0])):
        tboard[0][i]+=tboard[0][i-1]
    for i in range(1, len(tboard)):
        tboard[i][0]+=tboard[i-1][0]
    for x in range(1, len(tboard)):
        for y in range(1, len(tboard[0])):
            tboard[x][y]+=tboard[x][y-1]+tboard[x-1][y]-tboard[x-1][y-1]

    print(tboard)
    ans = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y]+tboard[x][y]>0: ans+=1
    return ans


if __name__ == '__main__':
    board1 = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill1 = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    # 답은 10
    print(solution(board1, skill1))