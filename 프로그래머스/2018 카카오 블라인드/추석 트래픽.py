def solution(lines):
  times = []
  for line in lines:
    end_time, duration = parse_date_to_mills(line)
    start_time = end_time - duration + 1
    times.append((start_time, end_time))

  # 시작 시간으로 정렬
  times.sort()

  max_count = 0
  for time in times:
    # 시작 시간으로부터 오른쪽
    low = time[0]; high = low + 999
    rcount = get_max(low, high, times)

    # 시작 시간으로부터 왼쪽
    high = low; low = high - 999
    lcount = get_max(low, high, times)

    max_count = max(max_count, rcount, lcount)

  return max_count

def get_max(low, high, times):
  count = 0
  for other in times:
    if in_process(low, high, other):
      count += 1

  return count

def in_process(low, high, time):
  start, end = time
  if end < low: return False
  if start > high: return False
  return True

def parse_date_to_mills(date):
  day, time, duration = date.split()
  hh, mm, ss = time.split(":")
  # 응답 완료 시간
  end_time = to_millis(hh, mm, ss)
  # 처리 시간
  duration = float(duration[:-1]) * 1000
  return int(end_time), int(duration)

def to_millis(hh, mm, ss):
  hh = int(hh); mm = int(mm);
  ss = float(ss)
  total = hh * 60 * 60 + mm * 60 + ss
  return total * 1000