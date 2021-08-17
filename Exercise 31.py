def int_input() -> int:
    valid = False
    while valid == False:
        try:
            number = input('>> ')
            if number.isdigit():
                if int(number) > 0:
                    valid = True
                    return int(number)
            else:
                print('You need to use positive numbers.')
        finally:
            pass


def karvonen_heart_rate(age, restingHR, intensity) -> int:
    intensity = intensity / 100
    return round((((220 - age) - restingHR) * intensity) + restingHR)


def heart_rate_range():
    # target is to print out bpm in range of intensities 55% to 95%
    intensity = 55
    
    print('What is your age?')
    age = int_input()
    print('What is your resting heart rate?')
    restingHR = int_input()

    print(f'Resting Pulse: {restingHR}  Age: {age}\nIntensity       Rate\n')
    while intensity != 100:
        targetHR = karvonen_heart_rate(age, restingHR, intensity)
        print(f'{intensity}%             {targetHR} bpm')
        intensity += 5


if __name__ == '__main__':
    heart_rate_range()
