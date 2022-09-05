king, queen, rook, bishop, knight, pawn = map(int, input().split())

if 1 - king != 0 :
    king = 1 - king
else :
    king = 0

if 1 - queen != 0 :
    queen = 1 - queen
else :
    queen = 0

if 2 - rook != 0 :
    rook = 2 - rook
else :
    rook = 0

if 2 - bishop != 0 :
    bishop = 2 - bishop
else :
    bishop = 0

if 2 - knight != 0 :
    knight = 2 - knight
else :
    knight = 0

if 8 - pawn != 0 :
    pawn = 8 - pawn
else :
    pawn = 0

print(f"{king} {queen} {rook} {bishop} {knight} {pawn}")
