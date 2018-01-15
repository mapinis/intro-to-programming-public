def wave_to_RGB(waveL):
    if(380 <= waveL <= 410):
        rgb = (0.6 - (0.41 * ((waveL - 380) / 30)), 
            0, 
            0.39 + (0.6 * ((waveL - 380) / 30)))
    elif(410 < waveL <= 440):
        rgb = (0.19 - (0.19 * ((waveL - 410) / 30)),
            0, 
            1)
    elif(440 < waveL <= 490):
        rgb = (0,
            1 - ((490 - waveL) / 50),
            1)
    elif(490 < waveL <= 510):
        rgb = (0,
            1,
            (510 - waveL) / 20)
    elif(510 < waveL <= 580):
        rgb = (1 - ((580 - waveL) / 70),
            1,
            0)
    elif(580 < waveL <= 640):
        rgb = (1,
            (640 - waveL) / 60,
            0)
    elif(640 < waveL <= 700):
        rgb = (1,
            0,
            0)
    elif(700 < waveL <= 780):
        rgb = (0.35 + (0.65 * ((780 - waveL) / 80)),
            0,
            0)
    else:
        print(waveL)
        print("Not in range")
        rgb = (0, 0, 0)

    return list(map(lambda x: int(x * 255), rgb))