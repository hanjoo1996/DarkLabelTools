# DarkLabelTools
DarkLabel 툴을 사용하여 라벨링 및 검수 작업을 할 때, excel 에 쉽게 정리하고 자동으로 라벨 정보 txt 파일을 수정해주는 기능들!

delete.py -> 실행시 object ID 를 입력하라는 명령이 나오고, object ID 입력시 .txt 파일 내 해당 옵젝을 다 지워줌.

update.py -> data.txt 파일에 시작 frame #, 끝나는 frame #, object ID, classification 순서대로 csv 형식으로 입력하여 저장.

그 후에 update.py 를 실행하면, 해당 frame 범위 안에 있는 해당 object ID 를 가진 DeepSORT 형식의 트래킹을 원하는 classification 으로 바꿔줌.

(보통 라벨링 시작을 할 때, DeepSORT 에서 인물 인식 object_tracker.py (from DeepSORT) 를 살짝 바꿔서 모든 감지된 인물 좌표 데이터를 WALK 로 라벨링 후, 
해당 인물이 다른 동작을 하고 있으면 바꿔주는게 더 편함으로 만든 기능이다)
