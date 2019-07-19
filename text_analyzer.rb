require 'pp'


def analyze(text)
 hash = {}
 return {} if text.empty?
 hash[:character_count] = character_count(text)
 hash[:character_count_excluding_spaces] = count_character_without_space(text)
 hash[:line_count] = count_lines(text)
 hash[:word_count] = count_words(text)
 hash[:paragraph_count] = paragraph_count(text)
 hash[:sentence_count] = sentence_count(text)
 hash[:average_sentences_per_paragraph] = average_word_paragraph(text)
 hash[:average_word_sentence] = average_word_sentence(text)
 puts hash.to_h
end

def character_count(text)
count = 0
text.chars.each {|element| count +=1}
count
end

def count_character_without_space(text)
count_words_without_space = 0
text.delete(" ").chars.each do |element|
  count_words_without_space += 1
end
count_words_without_space
end

def count_lines(text)
count_lines = 0
text.gsub(" ","").split.each {|element| count_lines += 1}
count_lines
end

def count_words(text)
count_words = 0
text.split.each do |element|
  count_words +=1
end
count_words
end

def paragraph_count(text)
check = text.split(/\n\n/).length
check
end

def sentence_count(text)
count_sentences = text.split(".").size
count_sentences
end

def average_word_paragraph(text)
solution = sentence_count(text).fdiv(paragraph_count(text)).round(2)
solution.to_f
end

def average_word_sentence(text)
solution = count_words(text).fdiv(sentence_count(text)).round(2)
solution.to_f
end

text ="Your name is Scrutis."
analyze(text)
