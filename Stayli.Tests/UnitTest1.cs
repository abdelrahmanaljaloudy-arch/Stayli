using Xunit;
using Stayli.App;

namespace Stayli.Tests;

public class UnitTest1
{
    [Fact]
    public void Add_ReturnsSum()
    {
        Assert.Equal(7, MathTools.Add(3, 4));
    }
}
