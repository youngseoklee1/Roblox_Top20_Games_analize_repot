# ==============================================================================
# PROJECT GENESIS: ROBLOX MARKET ANALYST BOT
# ==============================================================================
# 📝 Technical Documentation (English): ./roblox_analyst_bot.md
# 📝 Technical Documentation (Korean) : ./roblox_analyst_bot.ko.md
# ==============================================================================



import os
import time
import requests
from datetime import datetime

class RobloxAnalystBot:
    def __init__(self, target_universe_ids):
        """
        target_universe_ids: 분석할 로블록스 게임의 Universe ID 리스트
        (주의: 플레이 시 브라우저 주소창에 뜨는 Place ID와는 다른 고유의 Universe ID 구조를 가집니다)
        """
        self.universe_ids = target_universe_ids
        self.output_dir = "market_analysis"
        
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def fetch_game_metadata(self, universe_id):
        url = f"https://games.roblox.com/v1/games?universeIds={universe_id}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json().get("data", [])
                return data[0] if data else None
        except Exception as e:
            print(f"[-] Metadata Fetch Error for {universe_id}: {e}")
        return None

    def fetch_game_passes(self, universe_id):
        # 공식 엔드포인트 양식에 따라 게임패스 리스트 로드
        url = f"https://games.roblox.com/v1/games/{universe_id}/game-passes?limit=50&sortOrder=Desc"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json().get("data", [])
        except Exception as e:
            print(f"[-] GamePasses Fetch Error for {universe_id}: {e}")
        return []

    def fetch_badges(self, universe_id):
        url = f"https://badges.roblox.com/v1/universes/{universe_id}/badges?limit=50&sortOrder=Desc"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json().get("data", [])
        except Exception as e:
            print(f"[-] Badges Fetch Error for {universe_id}: {e}")
        return []

    def generate_markdown_report(self, meta, passes, badges):
        if not meta:
            return
        
        name = meta.get("name", "Unknown_Game").replace("/", "_").replace(" ", "_")
        universe_id = meta.get("id")
        
        # 유저 평점 계산 공식 산출
        allowed_votes = meta.get("allowedVotes", 0)
        upvotes = meta.get("upVotes", 0)
        downvotes = meta.get("downVotes", 0)
        total_votes = upvotes + downvotes
        upvote_ratio = (upvotes / total_votes * 100) if total_votes > 0 else 0
        
        filename = f"{self.output_dir}/auto_{name}_{universe_id}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# [Automated Report] {meta.get('name')} (Universe ID: {universe_id})\n\n")
            f.write(f"- **Generated At**: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n")
            f.write(f"- **Genre / Description Summary**: {meta.get('description', 'No description available.')[:200]}...\n\n")
            
            f.write("## 📊 1. 정량적 실시간 트래픽 지표 (Quantitative Metrics)\n")
            f.write(f"* **Current Live Players (CCU)**: {meta.get('playing', 0):,}\n")
            f.write(f"* **Total Cumulative Visits**: {meta.get('visits', 0):,}\n")
            f.write(f"* **Approval Rating (Upvote Ratio)**: {upvote_ratio:.2f}% (Up: {upvotes:,} / Down: {downvotes:,})\n")
            f.write(f"* **Last Updated Timestamp**: {meta.get('updated', 'Unknown')}\n\n")
            
            f.write("## 💰 2. 비즈니스 모델 정전 조사 (Monetization: Game Passes)\n")
            if not passes:
                f.write("* 판매 중인 공식 게임패스가 없거나 비공개 상태입니다.\n")
            else:
                f.write(f"현재 총 **{len(passes)}개**의 게임패스가 활성화되어 경제 구조를 견인하고 있습니다.\n\n")
                f.write("| 패스 명칭 (Pass Name) | 가격 (Robux) | 세부 기획 의도 설명 (Description) |\n")
                f.write("| :--- | :--- | :--- |\n")
                for p in passes:
                    pass_desc = p.get('description', 'No description').replace('\n', ' ')
                    f.write(f"| {p.get('name')} | {p.get('price', 'Free'):,} | {pass_desc} |\n")
            f.write("\n")
            
            f.write("## 📜 3. 유저 리텐션 배지 아키텍처 (Retention Engine: Badges)\n")
            if not badges:
                f.write("* 연동된 업적/배지 시스템 정보가 확인되지 않습니다.\n")
            else:
                f.write(f"총 **{len(badges)}개**의 마일스톤 배지를 활용해 유저 흐름과 이탈방지 장치 구축 상태를 트래킹합니다.\n\n")
                f.write("| 배지 명칭 (Badge Name) | 획득 유저 수 (Awarded) | 리텐션 기획 분석 의미 |\n")
                f.write("| :--- | :--- | :--- |\n")
                for b in badges:
                    statistics = b.get('statistics', {})
                    awarded = statistics.get('pastWeekAwardedCount', 0)
                    f.write(f"| {b.get('name')} | 지난주 {awarded:,}회 획득 | {b.get('description', 'No summary').replace('\n', ' ')} |\n")
            f.write("\n")
            
            f.write("## 🧠 4. 개발 3대 헌법 관점의 알고리즘 매칭 추론 (Strategic Audit)\n")
            f.write(f"1. **Engagement Assessment**: 본 게임은 실시간 동접 {meta.get('playing', 0):,}명을 기록 중이며, ")
            if upvote_ratio >= 90:
                f.write(f"평점 {upvote_ratio:.2f}%로 매우 견고한 유저 로열티를 확보함. 9~15분 체류 기준 충족 가능성 농후.\n")
            else:
                f.write(f"평점 {upvote_ratio:.2f}%로 유저 반발 요소 혹은 버그가 존재함. 플레이 타임 하락 리스크 모니터링 필요.\n")
            
            f.write(f"2. **Monetization Assessment**: 활성화된 패스 수 {len(passes)}개를 바탕으로 유저당 결제 단가(ARPPU) 유도 지점 고도화 여부 추적 가능.\n")
            f.write(f"3. **Retention Assessment**: 배지 획득 추이를 기반으로 코어 루프의 중독성과 장기 플레이 보상 체계 분석 완료.\n")

        print(f"[+] Report generated successfully: {filename}")

    def run(self):
        print("[*] Starting automated Roblox marketplace data-mining agent...")
        for uid in self.universe_ids:
            print(f"[*] Processing Universe ID: {uid}...")
            meta = self.fetch_game_metadata(uid)
            time.sleep(0.5) # API 과부하 방지용 딜레이 규칙 준수
            passes = self.fetch_game_passes(uid)
            time.sleep(0.5)
            badges = self.fetch_game_badges_or_similar = self.fetch_badges(uid)
            
            if meta:
                self.generate_markdown_report(meta, passes, badges)
            time.sleep(1)

if __name__ == "__main__":
    # 테스트용 샘플 대형 게임 Universe ID 리스트
    # 130521013 -> Brookhaven RP의 고유 Universe ID 예시
    # 2317109614 -> Blox Fruits의 고유 Universe ID 예시
    sample_universe_ids = [130521013, 2317109614]
    
    bot = RobloxAnalystBot(sample_universe_ids)
    bot.run()