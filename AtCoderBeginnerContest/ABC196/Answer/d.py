H, W, A, B = map(int, input().split())

# 畳で埋まっているかどうかを記録
used = [[False]*W for _ in range(H)]

def dfs(i, j, a, b):
    # どちらかの畳を使い切る
    if a < 0 or b < 0:
        return 0
    # 一番右に来た時に、左端に戻しつつ下を見る
    if j == W:
        j = 0
        i += 1
    # 一番下に到達したら終了
    if i == H:
        return 1
    # 畳で埋まってたら右となりを探索
    if used[i][j]:
        return dfs(i, j+1, a, b)
    res = 0
    used[i][j] = True
    # 半畳を使った場合
    res += dfs(i, j+1, a, b-1)
    # 横にAを置く場合
    # j+1がWに収まっていて、i, j+1が埋まってない
    if j + 1 < W and (not used[i][j+1]):
        used[i][j+1] = True
        res += dfs(i, j+1, a-1, b)
        # 1つ上の深さに戻るので未使用にする
        used[i][j+1] = False
    # 縦にAを置く場合
    # i+1がHに収まっていて、i+1, jが埋まってない
    if i + 1 < H and (not used[i+1][j]):
        used[i+1][j] = True
        res += dfs(i, j+1, a-1, b)
        # 一つ上の深さに戻るので未使用にする
        used[i+1][j] = False
    used[i][j] = False
    return res

print(dfs(0, 0, A, B))