def generate_summaries(self, num_articles=5, model="gpt-3.5-turbo"):
    """Generate summaries using OpenAI"""
    try:
        if not self.news_data:
            st.warning("No news data to summarize")
            return []
        
        if not os.getenv('OPENAI_API_KEY'):
            st.error("OpenAI API key not found")
            return []
        
        # Initialize the OpenAI client
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))  # Pass API key here
        
        self.summaries = []
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        sorted_articles = sorted(
            self.news_data, 
            key=lambda x: x.get('datetime', ''), 
            reverse=True
        )[:num_articles]
        
        for i, article in enumerate(sorted_articles):
            status_text.text(f"Summarizing article {i+1}/{num_articles}...")
            progress_bar.progress((i + 1) / num_articles)
            
            prompt = (
                f"Summarize this news article in 2-3 sentences:\n\n"
                f"Title: {article['title']}\n"
                f"Source: {article['media']}\n"
                f"Date: {article['date']}\n"
                f"Description: {article['desc']}\n\n"
                f"Summary:"
            )
            
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are a news summarizer."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3
                )
                
                summary = response.choices[0].message.content
                self.summaries.append({
                    'title': article['title'],
                    'source': article['media'],
                    'date': article['date'],
                    'summary': summary,
                    'link': article['link']
                })
                
                time.sleep(1)  # Rate limiting
            
            except Exception as e:
                st.warning(f"Couldn't summarize article: {str(e)}")
                continue
        
        # Save summaries
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        summary_file = SUMMARIES_DIR / f"summaries_{timestamp}.json"
        with open(summary_file, 'w') as f:
            json.dump(self.summaries, f)
        
        status_text.empty()
        progress_bar.empty()
        st.success(f"Generated {len(self.summaries)} summaries!")
        return self.summaries
    
    except Exception as e:
        st.error(f"Summary generation failed: {str(e)}")
        return []