CXX := g++
CXXFLAGS := -std=c++17 -Wall -O2 -MMD -MP

SRCDIR := .
SRCS := $(wildcard $(SRCDIR)/*.cpp)
OBJDIR := build
OBJS := $(patsubst $(SRCDIR)/%.cpp,$(OBJDIR)/%.o,$(SRCS))
DEPS := $(OBJS:.o=.d)

TARGET := cracking_coding_interview

.PHONY: all clean run

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp | $(OBJDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(OBJDIR):
	mkdir -p $(OBJDIR)

run: all
	./$(TARGET) $(ARGS)

clean:
	rm -rf $(OBJDIR) $(TARGET)

-include $(DEPS)
