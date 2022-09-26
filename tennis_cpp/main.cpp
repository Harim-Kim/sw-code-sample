/**
1. 아래 코드를 보고 분석해 주세요.
2. 코드를 보고 무슨 역할을 하는지 설명 해 보세요.
3. 해당 코드에서 잘 정의된 부분과 아닌 부분을 설명해 보세요.
4. 개선하면 좋은 부분을 찾아서 개선해 보세요.
*/

#include <string>

const std::string tennis_score(int p1Score, int p2Score) {
    std::string score = "";
    int tempScore=0;
    if (p1Score==p2Score)
    {
        switch (p1Score)
        {
            case 0:
                    score = "Love-All";
                break;
            case 1:
                    score = "Fifteen-All";
                break;
            case 2:
                    score = "Thirty-All";
                break;
            default:
                    score = "Deuce";
                break;

        }
    }
    else if (p1Score>=4 || p2Score>=4)
    {
        int minusResult = p1Score-p2Score;
        if (minusResult==1) score ="Advantage player1";
        else if (minusResult ==-1) score ="Advantage player2";
        else if (minusResult>=2) score = "Win for player1";
        else score ="Win for player2";
    }
    else
    {
        for (int i=1; i<3; i++)
        {
            if (i==1) tempScore = p1Score;
            else { score+="-"; tempScore = p2Score;}
            switch(tempScore)
            {
                case 0:
                    score+="Love";
                    break;
                case 1:
                    score+="Fifteen";
                    break;
                case 2:
                    score+="Thirty";
                    break;
                case 3:
                    score+="Forty";
                    break;
            }
        }
    }
    return score;
    
}
