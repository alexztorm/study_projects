def check_stop(minim, maxim, cur):
    if cur == minim == maxim + 1:
        return True
    else:
        return False


def update_min(new_val, old_min):
    if new_val < old_min:
        return new_val
    else:
        return old_min


def update_max(new_val, old_max):
    if new_val > old_max:
        return new_val
    else:
        return old_max


start_value = 8
step = int(start_value / 2)
wet_count = 0
max_wet, min_ok = 0, 10 ** 18
new_value = start_value
op_count = 1

print(new_value, flush=True)

new_command = input()

while new_command != "fail" or op_count < 200:
    op_count += 1
    if new_command == "ok":
        min_ok = update_min(new_value, min_ok)
        if check_stop(min_ok, max_wet, new_value):
            print("!", new_value)
            break
        if wet_count == 1:
            step //= 2
        wet_count = 0
        new_value = max(new_value - step, max_wet + 1)
        print(new_value, flush=True)
        new_command = input()
    elif new_command == "wet":
        max_wet = update_max(new_value, max_wet)
        if wet_count == 0:
            step //= 2
        else:
            step += wet_count ** (op_count % wet_count)
        wet_count += 1
        new_value = new_value + step
        print(new_value, flush=True)
        new_command = input()
