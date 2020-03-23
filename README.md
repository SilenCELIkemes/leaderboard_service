# leaderboard_service
## 接口 /score：
- 入参（c_id 客户端ID， c_score 分数）
    例：{"params":{"params": {"c_id":9, "c_score":132}}}
- 返回
    {
    "status": true,
    "error_message": "SUCCESSFUL"
}
## 接口 /search：
- 入参 （begin_point 排名起， end_point 排名至， c_id 客户端ID）
{"params":{"params": {"c_id":5, "begin_point":3,"end_point":5}}}
-返回
{
    "status": true,
    "dara": [
        {
            "c_id": 5,
            "c_score": 888
        },
        {
            "c_id": 4,
            "c_score": 777
        },
        {
            "c_id": 5,
            "c_score": 888
        }
    ]
}