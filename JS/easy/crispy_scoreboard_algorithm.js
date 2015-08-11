var newFen = 'rnbqkbnr/pppp2pp/8/8/8/3p4/PPP2PPP/RNB2BNR';
var oldFen = 'rnbqkbnr/pppp1ppp/8/8/8/3K4/PPP2PPP/RNB2BNR';

function isLetter(str) {
  return str.length === 1 && str.match(/[a-z]/i);
}

function pieceCount(fenStr) {
    var pieceCount = new Array();
    pieceCount = {
        'r': 0,
        'n': 0,
        'b': 0,
        'q': 0,
        'k': 0,
        'p': 0,
        'R': 0,
        'N': 0,
        'B': 0,
        'Q': 0,
        'K': 0,
        'P': 0
    };
    for (var i = 0; i < fenStr.length; i++){
        if (isLetter(fenStr[i])) {
            pieceCount[fenStr[i]] += 1
        }
    }
    return pieceCount;
}

function comparePieceCount(){
    var oldFenPieces = pieceCount(oldFen);
    var newFenPieces = pieceCount(newFen);
    var whiteScore = 0;
    var blackScore = 0;
    // standard point values https://en.wikipedia.org/wiki/Chess_piece_relative_value
    var pointValues = {
        'p': 1,
        'k': 3,
        'b': 3,
        'r': 5,
        'q': 9
    }
    for(key in oldFenPieces){
        if (oldFenPieces[key] != newFenPieces[key]){
            var difference = newFenPieces[key] - oldFenPieces[key];
            console.log("piece: " + key + " old count: " + oldFenPieces[key] + " new count: " + newFenPieces[key])
            //if piece is lowercase it's a black piece
            if (key == key.toLowerCase()) {
                blackScore += pointValues[key];
            } else if (key == key.toUpperCase()) {
                key = key.toLowerCase();
                whiteScore += pointValues[key];
            }
        }
    }
    return {'whiteScore': whiteScore, 'blackScore': blackScore}
}

console.log(comparePieceCount());


// black is lowercase
// white is UPPERCASE
