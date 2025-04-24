import os
from pathlib import Path
from typing import Dict, Optional, Tuple
import json
from datetime import datetime

class GitaBot:
    def __init__(self):
        self.data_path = Path(__file__).parent.parent / "data"
        self._chapter_cache = {}
        
        # Reuse your BG_CHAPTER_INFO here
        self.chapter_info = {
            1: {'total_verses': 46, 'grouped_ranges': [(16, 18), (21, 22), (32, 35), (37, 38)], 'chapter_title': 'First. Observing the Armies...'},
            # ... rest of your chapter info
        }

    def _load_chapter_data(self, chapter: int) -> dict:
        """Load chapter data with caching"""
        if chapter in self._chapter_cache:
            return self._chapter_cache[chapter]
            
        file_path = self.data_path / f"bg_ch{chapter:02d}.json"
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self._chapter_cache[chapter] = data
            return data

    def _validate_verse(self, chapter: int, verse: str) -> Tuple[bool, str]:
        """Your existing validation logic"""
        # ... (same as in your Discord cog)
        
    def _format_verse_text(self, chapter: int, verse_ref: str) -> str:
        """Format verse for Telegram message"""
        chapter_data = self._load_chapter_data(chapter)
        verse_data = self._find_verse_data(chapter_data, verse_ref)
        
        # Reuse your formatting logic from Discord cog
        text = f"*Chapter {chapter}: {self.chapter_info[chapter]['chapter_title']}*\n\n"
        text += f"*TEXT {verse_ref}:*\n{verse_data['Verse-Text']}\n\n"
        text += f"*TRANSLATION:*\n{verse_data['Translation-En']}"
        
        return text

    def get_navigation_buttons(self, chapter: int, verse_ref: str) -> Dict[str, Tuple[int, str]]:
        """Calculate previous/next verse targets"""
        # Reuse your navigation logic from NavigationButtons class
        prev_chapter, prev_verse = self._get_previous_verse(chapter, verse_ref)
        next_chapter, next_verse = self._get_next_verse(chapter, verse_ref)
        
        return {
            'prev': (prev_chapter, prev_verse) if prev_chapter else None,
            'next': (next_chapter, next_verse) if next_chapter else None
        }
