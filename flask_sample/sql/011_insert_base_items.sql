INSERT INTO
    IS601_S_Products (
        id,
        name,
        description,
        stock,
        unit_price
        /*image*/
    )
VALUES (
        -1,
        "Hair Dryer",
        "Dry your hair in seconds",
        9999999,
        10
        
    ), (
        -2,
        "Instant noodles",
        "2 minutes noodles",
        9999999,
        15
        
    ), (
        -3,
        "Summer Shorts",
        "Feel free in summmer",
        9999999,
        5
        
    ), (
        -4,
        "Bed Sheets",
        "Feels like silk",
        9999999,
        20
        
    ), (
        -5,
        "Healthy Chocolate",
        "Live healthy life",
        9999999,
        1
        
    ) ON DUPLICATE KEY
UPDATE
    modified = CURRENT_TIMESTAMP()