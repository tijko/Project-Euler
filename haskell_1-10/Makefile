.PHONY: default

TARGET=$(if $(problem),$(problem)).hs

default:
	ghc $(TARGET) -o $(if $(problem),$(problem))

clean:
	$(shell rm *.o && rm *.hi)
