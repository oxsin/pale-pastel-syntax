class Applicative m => Monad m where
    (>>=) :: m a -> (a -> m b) -> m b
    (>>) :: forall a b. m a -> m b -> m b
    return :: a -> m a
    return = pure

{-# SPECIALISE (=<<) :: (a -> [b]) -> [a] -> [b] #-}
(=<<)           :: Monad m => (a -> m b) -> m a -> m b
f =<< x         = x >>= f
