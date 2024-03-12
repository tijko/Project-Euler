.PHONY: default

TARGET=$(if $(problem),$(problem)).hs

default:
	ghc $(TARGET) -o $(if $(problem),$(problem)) -dynamic

clean:
	$(shell rm *.o && rm *.hi)
